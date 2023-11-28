from tokenizers import BertWordPieceTokenizer

wordpiece_tokenizer = BertWordPieceTokenizer(lowercase=False)
wordpiece_tokenizer.train(
    files=["./content/train.txt"],
    vocab_size=10000
)

wordpiece_tokenizer.save_model("./")
