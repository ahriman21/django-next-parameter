# login view : get 'next' param
class LoginView(View):
  def setUp(self,request,*args,**kwargs):
    self.next = request.GET['next']
    return super().setup(requet,*args,**kwargs)
  
  def get(self,request):
    # ...
    # your code 
    pass
  
  def post(self,request):
    # ...
    # write your codes and after it is done when you want to redirect your user do this :
    if self.next :
      return redirect(self.next)
    return redirect('home')
  return render(request,template_name,conttext)
    
