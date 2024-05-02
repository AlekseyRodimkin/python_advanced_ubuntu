from typing import List, Optional
import datetime
from flask import Flask, request
import math
import itertools

app = Flask(__name__)


@app.route(
    "/search/", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)
    if cell_tower_ids[0] <= 0:
        return f"Invalid cell_tower_id", 400

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    date_from: str = request.args.get("date_from", type=str, default=None)
    if date_from:
        try:
            datetime.datetime.strptime(date_from, '%Y%m%d')
        except ValueError:
            return f"Invalid date_from", 400

    date_to: str = request.args.get("date_to", type=str, default=None)
    if date_to:
        try:
            d_from = datetime.datetime.strptime(date_from, '%Y%m%d')
            d_to = datetime.datetime.strptime(date_to, '%Y%m%d')
            if d_from > d_to or date_to[4:6] > datetime.datetime.now().strftime('%m'):
                raise ValueError
            if date_to[4:6] == datetime.datetime.now().strftime('%m') and date_to[6:8] > datetime.datetime.now().strftime('%d'):
                raise ValueError
        except ValueError:
            return f"Invalid date`s", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    if len(phone_prefixes[0]) <= 10 and phone_prefixes[0][-1:] == '*':
        for value in phone_prefixes[0][:-1]:
            if not value.isdigit():
                return f"Invalid phone_prefix (symbol in prefix)", 400
    else:
        return f"Invalid phone_prefix", 400

    protocols: List[str] = request.args.getlist("protocol")
    if protocols[0] not in ("2G", "3G", "4G", "5G"):
        return f"Invalid protocol", 400

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}, "
        f"date_from={date_from}, "
        f"date_to={date_to}"
    )


@app.route("/sum-prod/", methods=["GET"])
def sum_and_product_numbers():
    numbers: List[int] = request.args.getlist("numbers", type=int)
    return f"{sum(numbers)}, {math.prod(numbers)}"


@app.route("/combinations/", methods=["GET"])
def combinations():
    nums_1: List[int] = request.args.getlist("number_1", type=int)
    nums_2: List[int] = request.args.getlist("number_2", type=int)
    return f"{list(itertools.product(nums_1, nums_2))}"


@app.route("/similar/", methods=["GET"])
def similar():
    numbers: List[int] = request.args.getlist("numbers", type=int)
    dad: int = request.args.get("dad", type=int)
    son: int = min(numbers, key=lambda x: abs(x - dad))
    return f"{son}"


if __name__ == "__main__":
    app.run(debug=True)
