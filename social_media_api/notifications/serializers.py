from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # To display the actor's username
    target = serializers.StringRelatedField()  # To display the target object (e.g., the post or comment)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'read', 'timestamp']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp']
