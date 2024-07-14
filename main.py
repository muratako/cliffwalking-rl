import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import worlddef
import actions
import learn

# エピソードの終了を定義
done_points = worlddef.done_points()

# 状態と行動のテーブルの初期状態を定義
theta_0 = actions.theta_0()

# ハイパーパラメータの設定
lr = 0.1
gamma = 0.9
epsilon = 0.5
episode = 1000

# 行動価値と方策を初期化
Q = np.random.rand(*theta_0.shape) * theta_0
pi_0 = actions.theta2pi(theta_0)

steps = []
rewards = []

for episode in range(episode):
    if epsilon < 1e-100:
        epsilon = 0.0
    else:
        epsilon /= 4
        
    h, r = learn.run(Q, epsilon, lr, gamma, pi_0, done_points)
    
    steps.append(len(h))
    rewards.append(r)

# ゴールしたエピソードと崖に落ちてしまったエピソードの取得
goal_episode = np.where(np.array(rewards)>0, 1, np.nan)
nongoal_episode = np.where(np.array(rewards)<0, 1, np.nan)

# 可視化
fig = plt.figure(figsize=(10, 5))
plt.scatter(x=np.arange(len(steps)), y=steps*goal_episode, c="b", s=15, label="success")
plt.scatter(x=np.arange(len(steps)), y=steps*nongoal_episode, c="r", s=15, label="failed")
plt.grid()
plt.legend(fontsize=30)
plt.show()

worlddef.plot_world(h)