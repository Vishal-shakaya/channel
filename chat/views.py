from django.shortcuts import render

# Create your views here.
def HomeView(request):
	return render(request, 'chat/CreateRoom.html')

def ChatRoom(request , room_name):
	context ={'room_name':room_name}
	return render(request, 'chat/Room.html', context=context)
