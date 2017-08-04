# What is it? / 概要
XCodeでWindows（3DS Maxなど）で吐出されたDAEファイルのテキスチャのパスがWindows方式になっているので、読み込めません。なので、これはDAEの中のファイルパスをUnix方式にするスクリプトです。

XCode can't read textures from DAE files exported in Windows (with programs like 3DX Max) as the file paths are saved in windows format. This script changes those paths to unix format.

# Usage / 使い方

`python daeFix.py < original.dae > fixed.dae`
