import numpy as np

# 状態と行動の表
def theta_0():
    # theta_0[状態, 行動] = 1 or np.nan
    # 行動は0：上に移動、1：右に移動、2：下に移動、3：左に移動を表す
    # theta_0の値が1なら行動選択可能、np.nanなら行動選択不可を表す
    theta_0 = np.ones((10*20, 4))

    # 選択不可能の行動を設定
    for i in range(20):
        theta_0[i][2] = np.nan  # 状態0～19（下端）では下移動を選択できない
        theta_0[-(i+1)][0] = np.nan  # 状態180～199（上端）では上移動を選択できない
    
    for i in range(10):
        theta_0[i*20][3] = np.nan  # 左端では左移動を選択できない
        theta_0[i*20+19][1] = np.nan  # 右端では右移動を選択できない

    return theta_0

# thetaを行動選択確率に変換
def theta2pi(theta):
    a, b = theta.shape
    pi = np.zeros((a, b))
    
    for i in range(a):
        pi[i] = theta[i] / np.nansum(theta[i])
        
    # np.nanを0に変換
    return np.nan_to_num(pi)

def get_action(s, Q, epsilon, pi):
    # Q関数から行動を選択
    # epsilonの確率でランダムに行動を選択
    if np.random.rand() < epsilon:
        action = np.random.choice(np.arange(4), p=pi[s])
    else:
        # 一番価値が高い行動を選択
        action = np.nanargmax(Q[s])
    return action

def get_next_state(s, a):
    # 行動から状態を変化させる
    if a == 0:
        # 上に移動
        next_state = s + 20
    elif a == 1:
        # 右に移動
        next_state = s + 1
    elif a == 2:
        # 下に移動
        next_state = s - 20
    else:
        # 左に移動
        next_state = s - 1
        
    return next_state

