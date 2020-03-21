# You will receive 3 lines of input. On the first line you will receive a title of an article.
# On the next line you will receive the content of that article. On the next n lines until you receive
# "end of comments" you will get the comments about the article. Print the whole information in html format.
# The title should be in "h1" tag (<h1></h1>); the content in article tag (<article></article>);
# each comment should be in div tag (<div></div>).


def print_title(text):
    return f"<h1>\n    {text}\n</h1>"


def print_content(text):
    return f"<article>\n    {text}\n</article>"


def print_comments(text):
    return f"<div>\n    {text}\n</div>"


title = input()
content = input()
comment = input()  # until "end of comments"


print(print_title(title))
print(print_content(content))
while comment != "end of comments":
    print(print_comments(comment))
    comment = input()
