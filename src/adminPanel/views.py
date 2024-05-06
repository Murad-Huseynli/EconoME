from django.shortcuts import redirect, render
from users.models import RegularUser


def requestsView(request):
    if request.user.is_anonymous or request.user.group != 'admin':
        return redirect('login-view')
    
    users = RegularUser.objects.filter(is_approved=False)
    template_name = 'adminPanel/requests.html'

    return render(request, template_name, {'users': users})


def requestDetail(request, pk):
    if request.user.is_anonymous or request.user.group != 'admin':
        return redirect('login-view')
    
    user = RegularUser.objects.get(id=pk)
     
    if request.method == 'POST' and 'approve' in request.POST:
        user.setApprove()
        
        return redirect('admin-requests-view')
    
    template_name = 'adminPanel/requestDetail.html'

    return render(request, template_name, {'user': user})
