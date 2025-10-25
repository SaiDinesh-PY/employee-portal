from rest_framework import serializers
class checkinserial(serializers.ModelSerializer):
    satisfaction_level=serializers.FloatField()
    last_evaluation=serializers.FloatField()
    number_project=serializers.IntegerField()
    average_montly_hours=serializers.IntegerField()
    time_spend_company=serializers.IntegerField()