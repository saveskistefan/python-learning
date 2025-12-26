name = input('Tell me your name: ')
movies = int(input('How many movies do you want: '))
movie_list = []

for i in range(movies):
    print(f'Movie {i+1}')
    movie_title = input('Movie title: ')
    rating = float(input('What is the ratig?: '))
    movie_list.append((movie_title,rating))

rate = []
for item in movie_list:
    rate.append(item[1])

total_movies = movies
average_rating = sum(rate) / len(rate)
highest_rating = max(rate)
lowest_rating = min(rate)

if average_rating >= 8:
    performance = 'You whatched top-quality movies'
elif average_rating >= 5:
    performance = 'Mixed experience'
else:
    performance = 'Bad movie week'

print(f'\n{name} whatched {movies} this week')

for movie_title,rating in movie_list:
    print(f'-{movie_title}: {rating} ')

print(f'\nAverage rating: {average_rating:.2f}')
print(f'Highest rating: {highest_rating}')
print(f'Lowest rating: {lowest_rating}')
print(f'\nReview: {performance}')

input('Press enter to exit')