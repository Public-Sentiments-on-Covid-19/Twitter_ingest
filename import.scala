import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.{StringType, IntegerType, DoubleType}

val spark = org.apache.spark.sql.SparkSession.builder.master("local").appName("Spark CSV Reader").getOrCreate;

val df = (spark.read.format("csv")
  .option("header", "true")
  .option("multiline","true")
  .option("mode", "DROPMALFORMED")
  //loads ALL data
  // .load("reddit_Data_H/reddit_Data/*.csv")
  //loads smaller sample data (1-20, 1-21, 3-18)
  .load("tweet_sentiment1.csv")
  )

var splitDF = (df.withColumn("Day",split(col("Date")," ").getItem(0))
  .withColumn("Tweet_VS",col("Tweet_VS").cast(DoubleType))
  .drop("Date"))
// splitDF.show()

val titleDF = splitDF.select("Tweet_VS", "Tweet","Date").dropDuplicates()
// titleDF.show(100)

// //Get how many (qualifying - 100 upvotes) posts are posted each day
// val postCountsDayDF = (titleDF.groupBy("Day")
//                     .count())
// postCountsDayDF.show()

//get the average qualifying post tweet sentiments each day
val averageTweetVSDayDF = (titleDF.groupBy("Date")
  .avg("Tweet_VS"))
averageTweetVSDayDF.show()
