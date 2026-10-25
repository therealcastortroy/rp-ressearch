
import lmdb

path = "data.mdb"

env = lmdb.open(
    path,
    subdir=False,
    readonly=True,
    lock=False,
)

with env.begin() as txn:
    for key, value in txn.cursor():
        print(f"\nKEY: {key!r}")
        try:
            print("VALUE:", value.decode("utf-8"))
        except UnicodeDecodeError:
            print("VALUE (hex):", value.hex()[:300])

env.close()

