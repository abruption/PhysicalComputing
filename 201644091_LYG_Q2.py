def music_info(artist, title):
    """
    음반 정보를 담은 리스트 만들기
    매개변수 : (아티스트, 노래제목)
    리턴 : 리스트
    """
    artists = []
    titles = []
    artists.append(artist.title())
    titles.append(title.title())
    return [artists, titles]





help(music_info)
print('프로그램 종료는 Q 또는 q')
while(True):
    song = input('\n지금 생각나는 노래는? ')
    if song.upper() == 'Q':
        break
    artist = input("위 노래를 부른 아티스트는? ")
    if artist.upper() == 'Q':
       break
    album = music_info(artist, song)
    print(album)
print("\n수고하셨습니다")