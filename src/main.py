import sys
import os
import time

def main():
    print("=== プログラム開始 ===")
    print("標準出力へのメッセージです")

    # 標準エラーへの出力
    print("エラー: 警告メッセージです", file=sys.stderr)

    # ファイル処理のシミュレーション
    print("ファイルを処理中...")
    time.sleep(1)

    try:
        # 存在しないファイルを開こうとしてエラーを発生させる
        with open("存在しないファイル.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません - {e}", file=sys.stderr)

    # 正常な処理
    print("データ処理が完了しました")
    print(f"現在のディレクトリ: {os.getcwd()}")

    # 複数行の出力
    for i in range(3):
        print(f"処理 {i+1}/3 完了")
        if i == 1:
            print(f"警告: 処理 {i+1} で軽微な問題が発生しました", file=sys.stderr)

    print("=== プログラム終了 ===")

    # 最後にエラーメッセージ
    print("注意: このプログラムはデモ用です", file=sys.stderr)

if __name__ == "__main__":
    main()
