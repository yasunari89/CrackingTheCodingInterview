

# 配列と文字列

## ハッシュテーブル
`index = hash(key) % len(array)`のようにindexが決められ、そのindexに連結リストが入っている。その連結リストからkeyに対応するvalueを取ってくる仕組み。

最悪ケースは`hash(key) % len(array)`が全て同じになってしまう場合で計算量はO(n)となるが、一般的な実装をすればO(1)となる。

## 配列リストと可変長配列

配列リスト（可変長配列）は計算量O(1)でのアクセスを備えつつ、自身のサイズを必要に応じて変更できる配列。一般的な実装では、配列がいっぱいになった時にサイズを2倍にする。**サイズを増やす処理自体は計算量O(n)**だが、処理回数的にはならしでO(1)となる。

## StringBuilder

文字列の+ operationは文字列サイズを増やす処理なので`words`が長さxの文字列をn個持っているとすれば、計算量はO(x+2x+...+nx) = O(xn^2)となり非効率。そこで`StringBuilder`を実装する。

しかしながら、Python3では+ operationのこの問題に対して内部で最適化されているため、あまり意味はなかった...

```python
def join_words(words):
  sentence = ''
  for word in words:
    sentence = sentence + word
  return sentence
```

```python
class StringBuilder:
  def __init__(self):
    self.string_list = [] 
  def append(self, string):
    self.string_list.append(string)  
  def to_str(self):
    return ''.join(self.string_list)

      
def join_words(words):
  sentence = StringBuilder()
  for word in words:
    sentence.append(word)
  return sentence.to_str()
```

## 文字コード（問題1.1）

- ASCII: 7bitなので全部で128種類
- Unicode: UTF-8とか。よくわからんけど8bit+16~32bitの可変長みたいな感じ？

## ソートするよりはループ（問題1.2）

string1とstring2で構成文字が同じかチェックする問題。

1. ソートして等しいか確認
2. ASCIIと仮定して文字の出現回数をハッシュテーブルで管理して確認

1だとソートでO(nlogn)の計算量がかかるが、2だとループだけなのでO(n)で済む。と思ったがPythonでやると1の方が高速なのはなぜだ...

