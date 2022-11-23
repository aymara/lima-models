#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author     Romaric Besançon (romaric.besancon@cea.fr)
# date       Mon May 17 2021
# copyright  Copyright (C) 2021 by CEA - LIST
#

import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np

from iso639 import languages

# ----------------------------------------------------------------------

# ad hoc additional languages not in iso639 library
LANGUAGES = {
    "Classical Chinese": "tc",  # not standard: 'traditional chinese'
    "Greek": "el",  # Greek, Modern
    "Kurmanji": "ku",  # Kurdish
    "Naija": "pcm",  # iso-639-2 of Nigerian Pidgin (?)
    "North Sami": "se",  # Northern Sami
    "Old French": "fro",  # iso-639-2
}


def get_language_code(lang):
    try:
        return languages.get(name=lang).alpha2
    except Exception:
        try:
            return LANGUAGES[lang]
        except KeyError as e:
            sys.stderr.write(f"Error: {str(e)}")
            return lang


# from https://stackoverflow.com/questions/33159134/matplotlib-y-axis-label-with-multiple-colors
def multicolor_label(ax, list_of_strings, list_of_colors, axis="x", anchorpad=0, **kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

    # x-axis label
    if axis == "x" or axis == "both":
        boxes = [
            TextArea(text, textprops=dict(color=color, ha="left", va="bottom", **kw))
            for text, color in zip(list_of_strings, list_of_colors)
        ]
        xbox = HPacker(children=boxes, align="center", pad=0, sep=5)
        anchored_xbox = AnchoredOffsetbox(
            loc=10,
            child=xbox,
            pad=0.0,
            frameon=False,
            bbox_to_anchor=(0.5, -0.11),
            bbox_transform=ax.transAxes,
            borderpad=0.0,
        )
        ax.add_artist(anchored_xbox)

    # y-axis label
    if axis == "y" or axis == "both":
        boxes = [
            TextArea(
                text,
                textprops=dict(color=color, ha="left", va="bottom", rotation=90, **kw),
            )
            for text, color in zip(list_of_strings[::-1], list_of_colors)
        ]
        ybox = VPacker(children=boxes, align="center", pad=0, sep=5)
        anchored_ybox = AnchoredOffsetbox(
            loc=3,
            child=ybox,
            pad=anchorpad,
            frameon=False,
            bbox_to_anchor=(-0.10, 0.2),
            bbox_transform=ax.transAxes,
            borderpad=0.0,
        )
        ax.add_artist(anchored_ybox)


class Result:
    def __init__(self, language, cols):
        self.language = language
        self.cols = cols
        self.data = {}

    def add_values(self, values):
        tool, mode = values[0], values[1]
        if tool not in self.data:
            self.data[tool] = {}
        self.data[tool][mode] = {}
        for i in range(2, len(values)):
            self.data[tool][mode][self.cols[i]] = float(values[i])

    def get_value(self, tool, mode, score):
        return self.data[tool][mode][score]


class Results:
    def __init__(self):
        self.data = {}

    def add_language(self, lang, cols):
        self.data[lang] = Result(lang, cols)

    def add_average(self, cols):
        self.avg_data = Result("AVG", cols)

    def add_average_values(self, values):
        self.avg_data.add_values(values)

    def add_values(self, lang, values):
        self.data[lang].add_values(values)

    def get_scores(self, labels, tool, mode, score):
        # return [self.data[l].get_value(tool,mode,score) for l in labels]
        scores = []
        for l in labels:
            try:
                scores.append(self.data[l].get_value(tool, mode, score))
            except KeyError:
                sys.stderr.write(
                    f"Error: failed to get score {score} for {tool}/{mode} "
                    f"for lang {l}\n"
                )
                scores.append(None)
        return scores

    def plot_bars(self, tool1, tool2, mode, score):
        labels, scores1, scores2 = self.prepare_data(tool1, tool2, mode, score)

        x = np.arange(len(labels))  # the label locations
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, scores1, width, label=tool1)
        rects2 = ax.bar(x + width / 2, scores2, width, label=tool2)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        plt.show()

    def prepare_data(self, tool1, tool2, mode, score):
        labels = sorted(self.data.keys())
        scores1 = self.get_scores(labels, tool1, mode, score)
        scores2 = self.get_scores(labels, tool2, mode, score)
        selected = [
            i
            for i in range(len(labels))
            if scores1[i] is not None and scores2[i] is not None
        ]
        labels = [f"{tool1}:{labels[i]}" for i in selected]
        scores1 = [scores1[i] for i in selected]
        scores2 = [scores2[i] for i in selected]
        return labels, scores1, scores2

    def get_label(self, label, selected_labels, filter_labels, use_full_names):
        """create the label according to the parameters"""
        # internal label has the form tool:label (see prepare_data above)
        tool, name = label.split(":")  # separator inserted in prepare_data
        if filter_labels is not None and tool != filter_labels:
            return None
        if selected_labels is not None and name not in selected_labels:
            return None
        if use_full_names:
            try:
                return languages.get(part3=name).name
            except KeyError:
                return name
        return name

    def plot_scatter(
        self,
        tool1,
        tool2,
        mode,
        score,
        with_average=False,
        with_labels=True,
        with_legend=True,
        grayscale=False,
        output_file=None,
        selected_labels=None,
        filter_labels=None,
        use_full_names=False,
    ):
        tools1 = []
        tools1_sizes = None  # if several tools in tool1, nb data for each
        tscores1, tscores2 = [], []
        if "," in tool1:
            labels, scores1, scores2 = [], [], []
            tools1 = tool1.split(",")
            tools1_sizes = []
            for i, t in enumerate(tools1):
                tlabels, s1, s2 = self.prepare_data(t, tool2, mode, score)
                tscores1.append(s1)
                tscores2.append(s2)
                labels += tlabels
                scores1 += s1
                scores2 += s2
                tools1_sizes.append(len(tlabels))
        else:
            labels, scores1, scores2 = self.prepare_data(tool1, tool2, mode, score)
        fig, ax = plt.subplots(figsize=(13.3, 6.9))
        colors = []
        if with_average:
            # add average values
            scores1.append(self.avg_data.get_value(tool1, mode, score))
            scores2.append(self.avg_data.get_value(tool2, mode, score))
            labels.append("AVG")
            s = [20] * len(labels)
            s[-1] = 500
        else:
            s = 80

        if tools1_sizes is not None:
            # several sources: use colors for sources
            if grayscale:
                selected_colors = ["#000000", "#888888", "#444444", "#cccccc"]
            else:
                # selected_colors = ["#2a5fdb", "#fa2f33", "#e82ad5", "#3ced2f"]
                selected_colors = ["#083eb9", "#fa2f33", "#e82ad5", "#3ced2f"]
                # selected_colors = ["#1a85ff", "#d41159", "#e82ad5", "#3ced2f"]
            selected_markers = ["o", "^", "s", "P"]  # circle,triangle,square,plus
            tcolors = []
            for i in range(len(tools1)):
                tcolors.append([selected_colors[i]] * tools1_sizes[i])
                colors += [selected_colors[i]] * tools1_sizes[i]
            # colored x_label
            ax.set_ylabel(tool2, fontsize=15)
            xlabels = tools1
            xcolors = selected_colors[: len(tools1)]
            # add '/' separator between tools
            xlabels = [i for s in zip(xlabels, ["/"] * len(xlabels)) for i in s][:-1]
            xcolors = [i for s in zip(xcolors, ["black"] * len(xcolors)) for i in s][
                :-1
            ]

            multicolor_label(ax, xlabels, xcolors, axis="x", size=15)
            # xboxes=[]
            # for i in range(len(tools1)):
            #     xboxes.append(TextArea(tools1[i], textprops=dict(color=selected_colors[i], size=15)))
            # xbox = HPacker(children=xboxes,align="center", pad=0, sep=5)
            # anchored_xbox = AnchoredOffsetbox(loc=3, child=xbox, pad=0.,
            #                                   frameon=False,
            #                                   bbox_to_anchor=(0.3, -0.07),
            #                                   bbox_transform=ax.transAxes, borderpad=0.)
            # ax.add_artist(anchored_xbox)

            for i, s1 in enumerate(tscores1):
                ax.scatter(
                    s1,
                    tscores2[i],
                    s=s,
                    c=tcolors[i],
                    marker=selected_markers[i],
                    label=f"{tool2} vs {tools1[i]}",
                )
        else:
            # use colors according to scores:
            # green if score(tool2)>score(tool1), red otherwise
            for i in range(len(labels)):
                if scores1[i] > scores2[i]:
                    colors.append("#ff0000")
                else:
                    colors.append("#00ff00")
            ax.set_xlabel(tool1, fontsize=15)
            ax.set_ylabel(tool2, fontsize=15)
            ax.scatter(scores1, scores2, s=s, c=colors)

        if with_labels:
            for i, txt in enumerate(labels):
                if selected_labels is None:
                    name = self.get_label(
                        txt, selected_labels, filter_labels, use_full_names
                    )
                    if name is not None:
                        ax.annotate(name, (scores1[i], scores2[i]))
                elif txt.startswith(filter_labels):
                    name = self.get_label(
                        txt, selected_labels, filter_labels, use_full_names
                    )
                    if name is not None:
                        # selected labels: use larger offset for the label
                        ax.annotate(
                            name,
                            (scores1[i], scores2[i]),
                            xytext=(5, 5),
                            textcoords="offset points",
                        )
        # zoom
        # ax.set_xlim(left=50)
        # ax.set_ylim(bottom=50)

        # log scale
        # ax.set_xscale('log')
        # ax.set_yscale('log')

        # plot median line
        ax.plot(range(100), range(100), c=colors[0])
        if with_legend:
            ax.legend()

        # force ratio
        # ratio = 0.5
        # xleft, xright = ax.get_xlim()
        # ybottom, ytop = ax.get_ylim()
        # ax.set_aspect(abs((xright - xleft) / (ybottom - ytop)) * ratio)

        if output_file is not None:
            plt.savefig(output_file)
        else:
            plt.show()


def draw_graphs(
    fin,
    output_file=None,
    score="LAS",
    tool="udify",
    mode="gold-tok",
    with_average=False,
    with_labels=True,
    with_legend=False,
    grayscale=False,
    selected_labels=None,
    filter_labels=None,
    use_full_names=False,
):
    results = Results()
    title, lang = "", ""
    in_table = False
    avg = False
    # languages = set()
    for line in fin:
        if line.startswith("###"):
            title = line.split()[1]
        elif line.startswith("| Tool | Mode"):
            elts = line.split()
            col_titles = [elts[i] for i in range(len(elts)) if i % 2 == 1]
            in_table = True
            if title == "Average":
                results.add_average(col_titles)
                avg = True
            else:
                avg = False
                # take language name from title
                # langname=title.split("-")[0].replace("\\_"," ")
                # if langname in languages:
                #     sys.stderr.write("Warning: multiple occurrences of language %s\n"%langname)
                # languages.add(langname)
                # lang=get_language_code(langname)
                # results.add_language(lang,col_titles)
        elif line.startswith("Download link: [lima-deep-models-"):
            # take language code from filename
            lang = line[33:36]
            results.add_language(lang, col_titles)
        elif in_table:
            elts = line.split()
            if len(elts) <= 1:
                in_table = False
                continue
            if elts[1] == "---":
                continue
            cols = [elts[i].replace("**", "") for i in range(len(elts)) if i % 2 == 1]
            if avg:
                results.add_average_values(cols)
            else:
                results.add_values(lang, cols)

    # for lang,res in results.data.items():
    #    print("%s:%s"%(lang,json.dumps(res.data)))
    # results.plot_bars(tool,"lima",mode,score)
    results.plot_scatter(
        tool,
        "lima",
        mode,
        score,
        with_average=with_average,
        with_labels=with_labels,
        with_legend=with_legend,
        grayscale=grayscale,
        output_file=output_file,
        selected_labels=selected_labels,
        filter_labels=filter_labels,
        use_full_names=use_full_names,
    )


# ----------------------------------------------------------------------
# main function
def main(argv):
    # parse command-line arguments
    parser = argparse.ArgumentParser(
        description="create a graph comparing the performance of LIMA to other tools, "
        "from the values taken in eval.md (a file such as eval.md is the expected "
        "input_file of this program)",
        epilog="""Example usages: 

# with labels

graphics.py --tool=udify,udpipe --output_file=eval.png eval.md 

# without labels

graphics.py --tool=udify,udpipe --no_labels --with_legend --output_file=eval.png eval.md 

# with some labels (command-line used to create the image in the LRE article)

graphics.py --tool=udify,udpipe --selected_labels=tha,bre,pcm,lzh,kmr,nno,gla,orv,uig,wol --with_legend --filter_labels=udify --use_full_names --output_file=lima_udify_udpipe.pdf eval.md


""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    # optional arguments
    parser.add_argument("--score", default="LAS", help="score to use (default is LAS)")
    parser.add_argument(
        "--tool", default="udify", help="score to use (default is udify)"
    )
    parser.add_argument(
        "--mode", default="gold-tok", help="score to use (default is gold-tok)"
    )
    parser.add_argument("--grayscale", action="store_true", help="use grayscale")
    parser.add_argument("--with_legend", action="store_true", help="add legend")
    parser.add_argument("--output_file", help="save the graph in the given file")
    parser.add_argument(
        "--no_labels", action="store_true", help="avoid language labels"
    )
    parser.add_argument(
        "--selected_labels",
        help="a comma separated list of languages for which the label should be kept",
    )
    parser.add_argument(
        "--filter_labels",
        help="if set, indicates the tool for which the labels are kept",
    )
    parser.add_argument(
        "--use_full_names",
        action="store_true",
        help="if set, use full names for the language labels",
    )
    # positional arguments
    parser.add_argument(
        "input_file", type=argparse.FileType("r", encoding="UTF-8"), help="input file"
    )

    param = parser.parse_args()

    with_labels = True
    if param.no_labels:
        with_labels = False

    selected_labels = None
    if param.selected_labels is not None:
        selected_labels = param.selected_labels.split(",")

    # do main
    draw_graphs(
        param.input_file,
        output_file=param.output_file,
        score=param.score,
        tool=param.tool,
        mode=param.mode,
        with_labels=with_labels,
        with_legend=param.with_legend,
        grayscale=param.grayscale,
        selected_labels=selected_labels,
        filter_labels=param.filter_labels,
        use_full_names=param.use_full_names,
    )


if __name__ == "__main__":
    main(sys.argv[1:])
