import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def main():
    calculated = 0
    unavailable = 0
    csv_path = Path(__file__).with_name("mansions.csv")

    with csv_path.open(encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            area = row["area_m2"].strip()
            if not area:
                result = "算出不可（面積空欄）"
                unavailable += 1
            else:
                unit_price = Decimal(row["price_man_yen"]) / Decimal(area)
                rounded_price = unit_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                result = f"{rounded_price:.2f} 万円/㎡"
                calculated += 1

            print(f"{row['id']}: {result}")

    print(f"算出{calculated}件、算出不可{unavailable}件")


if __name__ == "__main__":
    main()
