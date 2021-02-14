def make_markdown_table(var):

    markdown = "```" + str("| ")

    for e in var:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(var)):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in var:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "```"