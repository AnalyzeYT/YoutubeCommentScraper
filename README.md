# YoutubeCommentScraper#
Welcome to the YouTube Comment Scraper repository! This project is designed to extract, process, and analyze YouTube comments and their interactions from videos on any YouTube channel. The scraper collects detailed information about comments, replies, and user engagement, providing a comprehensive dataset for further analysis.

### Features

- **Video Information Extraction:**
  - Retrieves metadata about videos including VideoID and upload date.
  
- **Comment Extraction:**
  - Extracts comments, including the number of likes and dislikes.
  
- **Reply Extraction:**
  - Captures replies to comments, including likes, dislikes, and the user IDs involved in the conversation.

- **Comprehensive Dataset:**
  - Compiles all extracted data into a structured dataset with the following columns:
    - `VideoID`: Unique identifier for each video.
    - `Channel`: Name of the YouTube channel.
    - `NumOfCommentlikes`: Number of likes a comment has received.
    - `NumOfCommentDislikes`: Number of dislikes a comment has received.
    - `NumOfReplies`: Number of replies to a comment.
    - `Comment`: The text of the comment.
    - `CommentedUserID`: Unique identifier for the user who commented.
    - `RepliedUserID`: Unique identifier for the user who replied to the comment.
    - `Reply`: The text of the reply.
    - `RepliesLikes`: Number of likes a reply has received.
    - `RepliesDislike`: Number of dislikes a reply has received.
    - `ToWhomTheyReplied`: The unique identifier of the user to whom the reply was directed.
    - `Comment|repliedTime`: The timestamp of when the comment or reply was posted.
    - `VideoUploadedtimeanddate`: The timestamp of when the video was uploaded.

### Applications

- **Sentiment Analysis:**
  - Analyze the sentiment of comments and replies to understand viewer reactions and opinions.

- **User Engagement Analysis:**
  - Investigate patterns of user engagement, including likes, dislikes, and reply interactions.

- **Community Management:**
  - Utilize the data to manage and engage with the community more effectively.

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/youtube-comment-scraper.git
   cd youtube-comment-scraper
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scraper:**
   ```bash
   python scraper.py
   ```

4. **View the Dataset:**
   - The extracted data will be saved in a CSV file for easy analysis.

Example : 
![image](https://github.com/user-attachments/assets/541416b8-bc14-44bc-8b74-d3fa1e5e28f4)
### Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information or to get in touch, please visit the [project's homepage](https://github.com/your-username/youtube-comment-scraper).

Happy scraping!
