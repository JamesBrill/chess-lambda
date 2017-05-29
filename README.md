### Chess Lambda

Serverless chess move recommender. Takes a URL-encoded chess board position in [Forsyth-Edwards Notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) in the API path and returns a good move to play from that position.

To add dependencies to the service, run `pip3 install -t vendored/ -r requirements.txt`.

If you want to test the function locally on a Mac, you'll need a binary for the chess engine called `stockfish_mac`. You can create this from the [Stockfish source code](https://stockfishchess.org/download/). If you're running on other operating systems and system architectures, make the appropriate binary and tweak the logic in the function that chooses which binary to use.
