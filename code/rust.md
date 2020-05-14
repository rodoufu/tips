# rust

## Running audit in the code

```sh
cargo install cargo-audit
cargo audit
```

## Static code check

```sh
ustup update
rustup component add clippy
cargo clippy
```

## Building the release version

```sh
cargo build --release
```

## Install nightly

```sh
rustup toolchain install nightly
cargo +nightly test
```

```sh
rustup install nightly
```

## Check for updates

Call the Python3 script [check_crates.py](check_crates.py).

