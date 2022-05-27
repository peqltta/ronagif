import os
for filename in os.listdir():
    if filename[-4:] == ".mp4":
        os.system(f'ffmpeg -i {filename} -vf "fps=24,scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -r 24 -s 350x350 {filename[:-4]}.gif')
