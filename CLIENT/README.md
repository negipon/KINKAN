# KINKAN - CLIENT

主にラズパイを使った勤怠管理システムの構築を目指し、このリポジトリではクライアントとなるラズパイ側のソースを管理いたします。

クライアント側は非接触のICカードリーダーで社員証や入館証などのカードを読み込み、その情報をAPIサーバーにリクエストするなどの機能を要します。

構成及び構成図は以下

* プログラム構成：Python + Flask + nfcpy
* ハード構成：ラズパイ + SONY 非接触ICカードリーダー/ライター PaSoRi(パソリ) USB対応 RC-S380

[構成図](https://docs.google.com/presentation/d/1yHO1l2jPXYEVpU1mHMT9XeNqnUcJoeeENTeV9Jl79Gc/edit?usp=sharing)



## Installation

1. Install Rasbian
2. Install pip
3. Install Bazaar
4. Install nfcpy

## Usage

#### 1. git pull
#### 2. pythonでapp.py起動
```sh
$ python app.py
```

## Contributing


## History

TODO: Write history
