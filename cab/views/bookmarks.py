from django.http import HttpResponseRedirect
from django.shortcut import get_object_or_404,render_to_resopnse
from django.contrib.auth.decorators import login_required
from cab.models import Bookmark,Snippet
from django.veiws.generic.list_detail import object_list

def add_bookmark(request,snippet_id):
	snippet = get_object_or_404(Snippet,pk=snippet_id)
	try:
		Bookmark.objects.get(user__pk=request.user.id,
							snippet__pk=snippet.id)
	except Bookmark.DoesNotExist:
		bookmark = Bookmark.objects.creat(user=request.user,
											snippet=snippet)
	return HttpResponseRedirect(snippet.get_absolute_url())
add_bookmark = login_required(add_bookmark)

def delete_bookmark(request,snippet_id):
	if request.method == 'POST':
		snippet = get_object_or_404(Snippet,pk=snippet_id)
		Bookmark.objects.filter(user__pk=request.user.id,
								snippet__pk=snippet.id).delete()
		return HttpResponseRedirect(snippet.get_absolute_url())
	else:
		return render_to_resopnse('cab/confirm_bookmark_delete.html',
									{'snippet':snippet })
delete_bookmark = login_required(delete_bookmark)


def user_bookmarks(request):
	return object_list(queryset=Bookmark.objects.filter(user__pk=request.user.id),
						template_name='cab/user_bookmarks.html',
						paginate_by=20)
