dy=[0,1,0,-1]
dx=[1,0,-1,0]
#→↓←↑

# 調べる全方向をforで回してそれぞれ走査、各方向につきその方向に突き進んでいく、
# はみ出るまでインクリメントなど、はみ出たらその方向はbreak

for d in range(4):#方向数
    y,x=#ここで元の座標などから暫定座標を取得
    while True:
        y+=dy[d]
        x+=dx[d]
        if True:#ここではみ出る判定
            #判定例 y<0 or H<=y or x<0 or W<=x or s[y][x]=='#' こんな感じで複数条件いっぺんに書いちゃおう
            break
        #判定に通った場合 ans+=1 など
