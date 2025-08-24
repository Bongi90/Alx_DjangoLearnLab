from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.user.id == user_id:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    if user_to_follow not in request.user.following.all():
        request.user.following.add(user_to_follow)
        return Response({"success": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

    return Response({"message": f"You are already following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.user.id == user_id:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    if user_to_unfollow in request.user.following.all():
        request.user.following.remove(user_to_unfollow)
        return Response({"success": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

    return Response({"message": f"You are not following {user_to_unfollow.username}."}, status=status.HTTP_200_OK)