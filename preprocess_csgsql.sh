cd data
rm -rf csgsql
rm -rf database-csgsql
rm tables.json
mkdir csgsql
unrar e sel5.rar csgsql/
rm csgsql/train.json
rm csgsql/dev.json
mv csgsql/train_data.json csgsql/train.json
mv csgsql/dev_data.json csgsql/dev.json
mv csgsql/db_schema.json csgsql/tables.json
cp csgsql/tables.json ./