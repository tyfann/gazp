mkdir gen-csgsql
python generate.py --num 50000 --fout gen-csgsql/gen1.json --resume exp/sql2nl/csgsql-r1/best.tar --fparser exp/nl2sql/csgsql-r1/best.tar
python generate.py --num 50000 --fout gen-csgsql/gen2.json --resume exp/sql2nl/csgsql-r1/best.tar --fparser exp/nl2sql/csgsql-r1/best.tar --seed 2