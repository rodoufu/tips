# go

## Get all dependencies

```sh
go get -u -v -f all
```

```sh
go mod download
```

## Update a specific dependency

```sh
go get -u https://github.com/go-resty/resty
go get -u https://github.com/go-aah/aah
```

## Removing unused dependencies

```sh
go mod tidy
```

## Update a dependency with for specific branch

```sh
go get -u github.com/modular-network/zabo-api-provider@develop github.com/modular-network/zabo-api-resources@develop
```

## Testing

```sh
go test -run ''      # Run all tests.
go test -run Foo     # Run top-level tests matching "Foo", such as "TestFooBar".
go test -run Foo/A=  # For top-level tests matching "Foo", run subtests matching "A=".
go test -run /A=1    # For all top-level tests, run subtests matching "A=1".
```

### Unit test

```go
func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

Running coverage tests:
```sh
go test -cover ./...
```

### Benchmarks

```go
func BenchmarkHello(b *testing.B) {
    for i := 0; i < b.N; i++ {
        fmt.Sprintf("hello")
    }
}
```

Running the benchmark tests:

```sh
go test -bench=. -run=Bench -v ./...
```
