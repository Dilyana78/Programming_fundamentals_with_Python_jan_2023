title = input()
content = input()
comments = []

while True:
    comment = input()
    if comment == "end of comments":
        break
    comments.append(comment)

print(f"""<h1>
    {title}
</h1>""")

print(f"""<article>
    {content}
</article>""")

for comment in comments:
    print(f"""<div>
    {comment}
</div>""")
