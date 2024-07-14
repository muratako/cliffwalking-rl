import numpy as np

import actions

def Q_learning(Q, s, a, r, s_next, lr, gamma, done):
    # 行動価値関数の更新
    if done:
        Q[s, a] = Q[s, a] + lr*(r - Q[s, a])
    else:
        Q[s, a] = Q[s, a] + lr*(r + gamma*np.nanmax(Q[s_next]) - Q[s, a])
    return Q

def run(Q, epsilon, lr, gamma, pi, done_points):
    s = 0  # 初期位置
    a_next = actions.get_action(s, Q, epsilon, pi)
    
    # 状態の遷移を記録
    state_history = []
    
    while True:
        a = a_next
        s_next = actions.get_next_state(s, a)
        
        if s_next == 19:
            # ゴールに遷移した場合
            r = 1
            a_next = np.nan
            done = True
        elif s_next in done_points:
            # ゴール以外の終了ポイントに遷移した場合
            r = -100
            a_next = np.nan
            done = True
        else:
            r = -1
            # 次の行動を取得
            a_next = actions.get_action(s_next, Q, epsilon, pi)
            done = False
        
        # Q関数を更新
        Q = Q_learning(Q, s, a, r, s_next, lr, gamma, done)
        state_history.append(s)
        
        if done:
            state_history.append(s_next)
            break
        else:
            s = s_next
            
    return state_history, r