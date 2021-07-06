from django.shortcuts import render
from django.views     import generic
from blog.models      import Article, Comment

class ArticlesView(generic.ListView):
    model = Article

    paginate_by = 10

def view_article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Article does not exist")

    if request.method == 'POST':
        comment = Comment(
            article=article,
            username=request.user.username,
            body=request.POST['comment_body']
        )

        comment.save()

    return render(request, 'blog/article.html', context={"article": article})
