import os
for filename in os.listdir():
    os.system(f'ffmpeg -i {filename} -vf "fps=24,scale=350:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -r 24 -s 350x350 {filename[:-4]}.gif')
