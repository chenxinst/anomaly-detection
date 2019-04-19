import argparse

parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
parser.add_argument("--path", required=True, type=str, help="csv path")
parser.add_argument("--cpu_id", default=-2, type=int, help="cpu_id")
parser.add_argument("--system_name", default="all", type=str, help="cpu_id")
parser.add_argument("--target", default="user_sys_pct", type=str, help="y")
parser.add_argument("--length", default=500, help="length of x")
parser.add_argument("--start", default=0, help="")


 