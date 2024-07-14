import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_world(steps=[]):
    fig = plt.figure(figsize=(10, 5))
    ax = plt.gca()

    # 描画範囲を指定
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 10)

    # グリッドの間隔を指定
    x_line = np.linspace(0, 20, 21)
    y_line = np.linspace(0, 10, 11)

    ax.set_xticks(x_line)
    ax.set_yticks(y_line)

    # マーキング
    _ = ax.plot([0.5], [0.5], marker="o", markersize=20, c="b")  # エージェント
    _ = ax.plot([19.5], [0.5], marker="D", markersize=15, c="orange")  # ゴール

    # 崖の描画
    for i in range(15):
        _ = ax.plot([3.5+i], [0.5], marker="x", markersize=20, c="r")
        _ = ax.plot([3.5+i], [1.5], marker="x", markersize=20, c="r")

    for i in range(20):
        _ = ax.plot([0.5+i], [8.5], marker="x", markersize=20, c="r")
        _ = ax.plot([0.5+i], [9.5], marker="x", markersize=20, c="r")

    bad_points_x = [9.5, 4.5, 14.5]
    bad_points_y = [2.5, 6.5, 6.5]
    for x, y in zip(bad_points_x, bad_points_y):
        _ = ax.plot([x], [y], marker="x", markersize=20, c="r")
        _ = ax.plot([x+1], [y], marker="x", markersize=20, c="r")
        _ = ax.plot([x], [y+1], marker="x", markersize=20, c="r")
        _ = ax.plot([x+1], [y+1], marker="x", markersize=20, c="r")

    for s in steps:
        x_agent = s % 20
        y_agent = s // 20
        _ = ax.plot([0.5+x_agent], [0.5+y_agent], marker="o", markersize=12, c="b")  # エージェント
    
    plt.grid()
    plt.show()

# エピソードを終了させる状態（崖とゴールの状態）を定義
def done_points():
    done_points = []

    for i in range(15):
        done_points.append(i+3)
        done_points.append(i+3+20)

    for i in range(20):
        done_points.append(20*8+i)
        done_points.append(20*9+i)

    point_x = [9, 4, 14]
    point_y = [2, 6, 6]

    for x, y in zip(point_x, point_y):
        done_points.append(20*y+x)
        done_points.append(20*y+(x+1))
        done_points.append(20*(y+1)+x)
        done_points.append(20*(y+1)+(x+1))

    # ゴール
    done_points.append(19)

    return done_points
