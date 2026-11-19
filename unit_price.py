import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def main():
    csv_path = Path(__file__).with_name("mansions.csv")
    calculated = 0
    missing_area = 0

    with csv_path.open(encoding="utf-8-sig", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            mansion_id = row["id"]
            area = row["area_m2"].strip()
            if not area:
                print(f"{mansion_id}: 算出不可（面積空欄）")
                missing_area += 1
                continue

            price = Decimal(row["price_man_yen"])
            unit_price = (price / Decimal(area)).quantize(
                Decimal("1"), rounding=ROUND_HALF_UP
            )
            print(f"{mansion_id}: {unit_price:.0f} 万円/㎡")
            calculated += 1

    print(f"算出{calculated}件、算出不可{missing_area}件")


if __name__ == "__main__":
    main()
