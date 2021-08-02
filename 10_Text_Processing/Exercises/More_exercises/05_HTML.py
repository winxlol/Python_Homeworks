title = input()
article = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {article}\n</article>")

while True:
    comments = input()

    if comments == "end of comments":
        break

    print(f"<div>\n    {comments}\n</div>")