import requests
import json
import base64

print('Creating playlist')

spotifyGetSong = 'https://api.spotify.com/v1/me/playlists'
accessToken = 'BQDgirYSljVtLRIcX0m1kFD2qH4Q4lex_eeNPwOZrjpnkKGMoQjMG7ERYtUDLH7WwmkrEnK1eFe-2Ps3F0AkHBBLsT2PcGmayGLTMGzqJnW1lTVgHV1_BopBjpCfLj589zArbifHLFYSOcKoosAFpfNn2B7q5jkyaeOhnjb2wB-1zGNvxmNq6j4ORIHq'


def GetSong():
    spotifyGetSong = 'https://api.spotify.com/v1/me/playlists'
    accessToken = 'BQDgirYSljVtLRIcX0m1kFD2qH4Q4lex_eeNPwOZrjpnkKGMoQjMG7ERYtUDLH7WwmkrEnK1eFe-2Ps3F0AkHBBLsT2PcGmayGLTMGzqJnW1lTVgHV1_BopBjpCfLj589zArbifHLFYSOcKoosAFpfNn2B7q5jkyaeOhnjb2wB-1zGNvxmNq6j4ORIHq'

   
    response = requests.get(
        spotifyGetSong,
        headers={"Authorization": f"Bearer {accessToken}"} 
    )
    print(response.json())
    jsondata = json.dumps(response.json())
    with open("spotifyplaylist.json", "w") as outfile:
        outfile.write(jsondata)
    return response.json()
    

def main():
    GetSong()

if __name__ == '__main__':
    main()

main()