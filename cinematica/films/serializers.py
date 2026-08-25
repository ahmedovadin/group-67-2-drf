from rest_framework import serializers
from .models import Film, Director, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        exclude = 'birthday'.split()

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    # genres = GenreSerializer(many=True)
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Film
        # fields = ['id', 'title', 'rating', 'created']
        # fields = '__all__'
        # exclude = ['text', 'updated']
        # fields = 'id title rating created director genres genre_list'.split()
        fields = 'id title rating created director genres reviews'.split()
        depth = 1
    
    def get_genres(self, film):
        # return [i.name for i in film.genres.all()]
        return film.genre_list()
