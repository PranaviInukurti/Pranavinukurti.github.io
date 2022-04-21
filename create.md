[Create Task Video](https://www.youtube.com/watch?v=t4xoukzHaFE)

[Written Responses](https://github.com/PranaviInukurti/Pranavinukurti.github.io/wiki/Create-Task-Plan)

[Runtime On Repl](https://replit.com/join/jryxtojgmf-pranaviinukurti)

HTML CODE:
  <!DOCTYPE html>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <head>
          <title>Which BLACKPINK Member Are You Quiz</title>
      </head>
      <style>
          body {
              background-image: url("/static/assets/blackpink5 (1).jpg/");
              font-family: Helvetica;
          }
          #main {
              width: 80%;
              max-width: 950px;
              border: 1px gray solid;
              margin: auto;
              padding: 10px;
              background-color: rgba(255,255,255, 0.8);
              border-radius: 10px;
          }
          #header {
              margin-top: 0;
              border: 2px solid black;
              padding: 280px;
              height: 250px;
              background: beige url("/static/assets/blackpink6.jpg/");
              color: white;
          }
          label {
              display: block;
              font-size: 25px;
              font-family: monospace;
          }
          input {
              width: 30px;
              margin-left: 20px;
          }
          h1 {
              font-size: 78px;
              margin-top: -180px;
              margin-left: -150px;
              font-family: monospace;
          }
          h2 {
              font-size: 30px;
              font-family: monospace;
          }
          p {
              font-size: 25px;
              font-family: monospace;
          }
          button {
              font-size: 25px;
              width: 125px;
              height: 50px;
              font-family: monospace;
          }

      </style>
      <body>

      <!- Background ->

      <div id="main"><!-- open main div -->
          <div id="header"><!-- open header div -->
              <h1>Which BLACKPINK Member Are You?</h1>
          </div><!-- close header div -->

          <center>

              <!- Quiz ->
              <form id="form1">
                  <h2>1. You're going out with friends for a small party, what are you going to wear?</h2>
                  <label for="style_1"><input type="radio" name="style" value="1" id="style_1" />Campus Style </label>
                  <label for="style_2"><input type="radio" name="style" value="2" id="style_2" />Sports Style</label>
                  <label for="style_3"><input type="radio" name="style" value="4" id="style_3" />Vintage Style</label>
                  <label for="vstyle_4"><input type="radio" name="style" value="3" id="style_4"/>Dark Style</label>
                  <!-- use name instead of id because id can only use once in a html-->
                  <!-- different amount of points (1, 2, 3 or 4) are stored behind different choices-->
                  <br><br><br><br><br><br>
                  <h2>2. You and your friends are now in the cafe, what will you order?</h2>
                  <label for="food_1"><input type="radio" name="food" value="2" id="food_1"/>Ice Cream<br></label>
                  <label for="food_2"><input type="radio" name="food" value="1" id="food_2"/>Date Cake<br></label>
                  <label for="food_3"><input type="radio" name="food" value="4" id="food_3" />French Fries<br></label>
                  <label for="food_4"><input type="radio" name="food" value="3" id="food_4" />Kimchi Soup<br></label>
                  <br><br><br><br><br><br>
                  <h2>3. You and your friends are chatting about, if you could date a BLACKPINK member, who would you date?</h2>
                  <label for="member_1"><input type="radio" name="member" value="3" id="member_1" />Jennie<br></label>
                  <label for="member_2"><input type="radio" name="member" value="4" id="member_2" />Lisa<br></label>
                  <label for="member_3"><input type="radio" name="member" value="2" id="member_3" />Jisoo<br></label>
                  <label for="member_4"><input type="radio" name="member" value="1" id="member_4" />Rose<br></label>
                  <br><br><br><br><br><br>
                  <h2>4. You've had enough to eat and drink, what do you decide to do next?</h2>
                  <label for="activity_1"><input type="radio" name="activity" value="2" id="activity_1" />Come to the yoga studio.</label>
                  <label for="activity_2"><input type="radio" name="activity" value="4" id="activity_2" />Shopping of course!</label>
                  <label for="activity_3"><input type="radio" name="activity" value="1" id="activity_3" />Watch a movie.</label>
                  <label for="activity_4"><input type="radio" name="activity"  value="3" id="activity_4" />Singing time.</label>
                  <br><br><br><br><br>
                  <button type="submit" value="Submit">Submit</button>
              </form>

              <p>You are: <span id="grade" style="display: none">__</span></p> <!-- display none because i don't want to display the total points the user got-->
              <p id="grade2"></p>
              <br><br><br><br><br><br>

              <!-BLACKPINK MV->
              <!-- kill this love -->
              <button id="mv1" onclick="displayVideo()" style="font-size: 22px; width: 190px; height: 65px;">Kill This Love</button>
              <div id="display-video" style="display: none">
                  <iframe width="420" height="345" src="https://www.youtube.com/embed/2S24-y0Ij3Y"></iframe>
                  <!--iframe specifies an inline frame, that means it is used to embed some other document within the current HTML document.-->
              </div>

              <!-- how you like that -->
              <button id="mv2" onclick="displayVideo2()" style="font-size: 22px; width: 190px; height: 65px;">How You Like That</button>
              <div id="display-video2" style="display: none">
                  <iframe width="420" height="345" src="https://www.youtube.com/embed/ioNng23DkIM"></iframe>
              </div>

              <!-- ddu-du-ddu-du -->
              <button id="mv3" onclick="displayVideo3()" style="font-size: 22px; width: 190px; height: 65px;">DDU-DU-DDU-DU</button>
              <div id="display-video3" style="display: none">
                  <iframe width="420" height="345" src="https://www.youtube.com/embed/IHNzOHi8sJs"></iframe>
              </div>

              <br><br><br><br><br><br>

              <!-Random BLACKPINK Fact Generator->
              <div>
                  <button onclick="newFact()" style="font-size: 18px; width: 250px; height: 85px;">Generate BLACKPINK Fact
                  </button>
                  <div id="factDisplay" style="font-size: 17px; font-family: monospace;">
                      <!-- Quotes will display here -->
                  </div>
              </div>
          </center>
      </div><!-- close main div -->
      </body>

      <script>
          document.getElementById("form1").onsubmit=function() {
              style = parseInt(document.querySelector('input[name = "style"]:checked').value);
              food = parseInt(document.querySelector('input[name = "food"]:checked').value);
              member = parseInt(document.querySelector('input[name = "member"]:checked').value);
              activity = parseInt(document.querySelector('input[name = "activity"]:checked').value);

              result = style + food + member + activity;  //calculate total, add points together

              document.getElementById("grade").innerHTML = result;
              //display member's name and picture after clicked submit button
              if (result == 4, 5, 6) {result2 = "Jisoo<br />"}; //if total point is between 4 and 6, you are jisoo
              if (result == 7, 8, 9) {result2 = "Jennie<br />"}; //if total point is between 7 and 9, you are jennie
              if (result == 10, 11, 12) {result2 = "Rose<br />"}; //if total point is between 10 and 12, you are rose
              if (result == 13, 14, 15, 16) {result2 = "Lisa<br />"}; //if total point is between 13 and 16, you are lisa
              document.getElementById("grade2").innerHTML = result2;


              return false; // required to not refresh the page; just leave this here
          } //this ends the submit function

          //random BLACKPINK facts
          var facts = [
              'In 2016, YG Entertainment revealed that the reason BLACKPINK was chosen was to dismantle the idea that the color “pink” is only used to portray prettiness or cuteness. With this new group of girls, they wanted to show that pink doesn’t just mean “pretty,” but also incredible talent and hard work.',
              'Jisoo is crazy for Pikachu.',
              'BLACKPINK is the highest-charting South Korean girl group of all time.',
              'The music video for BLACKPINK’s single “Ddu-Du Ddu-Du” holds the record for the most-viewed music video by a K-Pop band.',
              'Lisa was so good that when she auditioned for YG in Thailand in 2010, she not only won first place but also beat out all of the competition. She ended up being the only candidate selected by the label at the time, as well as the first non-Korean artist to work at YG.',
              'BLACKPINK have their own reality TV show called BLACKPINK House, which follows the daily lives of the girls with a little bit of YG spice thrown in.',
              'BLACKPINK has BLINKS. A clever combination of Black and Pink, BLINKs are responsible for continually helping the girl group break records, especially on YouTube. For example, their smash hit Ddu-Du Ddu-Du garnered 36.2 million views in its first 24 hours.',
              'BLACKPINK was originally supposed to have 9 members. Interestingly enough, one of those cut trainees was none other than (G)I-DLE’s Miyeon!' ,
              'BLACKPINK has also been able to make big moves on the global stage, thanks to the unique background of each member. For example, Rosé was born in New Zealand and grew up in Australia, while Jennie went to school in New Zealand for a number of years. Lisa grew up in Thailand, and Jisoo was raised in South Korea.',
              'Between the 4 members, they can speak a number of languages besides Korean, like Japanese, English, Thai, and Mandarin. These language skills allow them to interact with more fans in more countries.',
              'BLACKPINK’s new single Kill This Love just casually beat out Ariana Grande’s thank u, next for the most views for a music video debut on YouTube within 24 hours, which was 56.7 MILLION VIEWS.',
              'Lisa’s step-father is none other than Marco Bruschweiler, a Master Chef and member of The World Association of Chefs’ Societies. He seems to be very supportive of Lisa, and has even made an appearance on BLACKPINK House, which moved Lisa to tears.'
          ]

          function newFact() {
              var randomNumber = Math.floor(Math.random() * (facts.length));
              document.getElementById('factDisplay').innerHTML = facts[randomNumber];
          }

          //click button to display BLACKPINK mv
          function displayVideo() {
              if($('#display-video').css('display') === 'none') $('#display-video').css('display', 'block')
              else $('#display-video').css('display', 'none')
          }
          function displayVideo2() {
              if($('#display-video2').css('display') === 'none') $('#display-video2').css('display', 'block')
              else $('#display-video2').css('display', 'none')
          }
          function displayVideo3() {
              if($('#display-video3').css('display') === 'none') $('#display-video3').css('display', 'block')
              else $('#display-video3').css('display', 'none')
          }
      </script>

CSS CODE: 
  h1 {
      text-align:center;
      font-family: monospace;
      font-size: larger;
      width: 65%;
      margin: 0 auto 5%;
      background-color: rgba(83,105,122, 0.8)
  }

  p {
      text-align:center;
      font-family: monospace;
      width: 65%;
      margin: 0 auto 5%;
      background-color: rgba(83,105,122, 0.8)
  }

  body {
      background-image: url('../../../static/assets/SAbg.jpg');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: cover;
      text-align:center;
      font-family: monospace;
      width: 65%;
      margin: 0 auto 5%;
      background-color: rgba(83,105,122, 0.8);
  }