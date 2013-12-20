<?php require("header.php"); ?>
<?php require("sidebar.php"); ?>
    <section id="content">
      <section class="vbox">
        <header class="header b-b bg-white">
          <div class="input-group input-s pull-right m-t-sm">
            <span class="input-group-addon input-sm"><i class="icon-search"></i></span>
            <input type="text" class="form-control input-sm" id="search-note" placeholder="search">
          </div>
          <div class="btn-group pull-left">
                <a href="dashboard.php" type="button" class="btn btn-sm btn-white"><i class="icon-chevron-left"></i> Back</a>
              </div>

        </header>
        <section class="scrollable wrapper">          
          <div class="row">
            <div class="col-sm-9">
              <div class="blog-post">
                <div class="post-item">
                 
                  <div class="caption wrapper-lg">
                    <h2 class="post-title"><a href="#">JQuery Distance Between Two Dates</a></h2>
		    <br>
                    <div class="post-sum">
                      <p>In this script, I've used Javascript to focus on creating something great with this two dates function. Check this out because this is example text that I'm writing about this specific script at around two o clock on wednesday. 
                      <br><br>
                      Phasellus at ultricies neque, quis malesuada augue. Donec eleifend condimentum nisl eu consectetur. Integer eleifend, nisl venenatis consequat iaculis, lectus arcu malesuada sem, dapibus porta quam lacus eu neque.</p>
		      <br>
		   
<div class="pull-right">
    <div class="m-b-sm">
                <div class="btn-group">
                  <a type="button" class="btn btn-white">Raw</a>
                  <a id="copy-script" type="button" class="btn btn-white">Quick Copy</a>
                </div>              
              </div>

</div>
<div class="span12">
<pre id="script" class="prettyprint lang-html ">
&lt;script type="text/javascript"&gt;
    // Say hello world until the user starts questioning
    // the meaningfulness of their existence.
    function helloWorld(world) {
      for (var i = 42; --i &gt;= 0;) {
	alert('Hello ' + String(world));
      }
    }
    &lt;/script&gt;
    &lt;style&gt;
    p { color: pink }
    b { color: blue }
    g { color: green }
    c { color: cyan }
    m { color: murple }
    u { color: "umber" }
&lt;/style&gt;
</pre>
</div>
		      
		      
                    </div>
		    
		  <div class="tags m-b-lg">
                <a href="#" class="label bg-success">JQuery</a> <a href="#" class="label bg-success">HTML</a> <a href="#" class="label bg-success">CSS</a> <a href="#" class="label bg-success">Less</a> <a href="#" class="label bg-success">Date</a> <a href="#" class="label bg-success">Scripts</a>
              </div>
                    <div class="line line-lg"></div>
                    <div class="text-muted">
                      <i class="icon-user icon-muted"></i> by <a href="#" class="m-r-sm">Nick</a>
                      <i class="icon-time icon-muted"></i> Nov 20, 2013
                      <a href="#" class="m-l-sm"><i class="icon-comment-alt icon-muted"></i> 4 comments</a>
                    </div>
                  </div>
                </div>
                
              </div>
              <h4 class="m-t-lg m-b">3 Comments</h4>
              <section class="comment-list block">
                <article id="comment-id-1" class="comment-item">
                  <a class="pull-left thumb-sm">
                    <img src="images/chris.jpg" class="img-rounded">
                  </a>
                  <section class="comment-body m-b">
                    <header>
                      <a href="#"><strong>Chris Favaloro</strong></a>
                      <label class="label bg-info m-l-xs">Editor</label> 
                      <span class="text-muted text-xs block m-t-xs">
                        24 minutes ago
                      </span>
                    </header>
                    <div class="m-t-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id neque quam. Aliquam sollicitudin venenatis ipsum ac feugiat. Vestibulum.</div>
                  </section>
                </article>
                <!-- .comment-reply -->
                <article id="comment-id-2" class="comment-item comment-reply">
                  <a class="pull-left thumb-sm">
                    <img src="images/avatar.jpg" class="img-rounded">
                  </a>
                  <section class="comment-body m-b">
                    <header>
                      <a href="#"><strong>John smith</strong></a>
                      <label class="label bg-dark m-l-xs">Admin</label> 
                      <span class="text-muted text-xs block m-t-xs">
                        26 minutes ago
                      </span>
                    </header>
                    <div class="m-t-sm">Lorem ipsum dolor sit amet, consecteter adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</div>
                  </section>
                </article>
                <!-- / .comment-reply -->
                <article id="comment-id-2" class="comment-item">
                  <a class="pull-left thumb-sm">
                    <img src="images/avatar.jpg" class="img-rounded">
                  </a>
                  <section class="comment-body m-b">
                    <header>
                      <a href="#"><strong>John smith</strong></a>
                      <label class="label bg-dark m-l-xs">Admin</label> 
                      <span class="text-muted text-xs block m-t-xs">
                        26 minutes ago
                      </span>
                    </header>
                    <blockquote class="m-t">
                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                      <small>Someone famous in <cite title="Source Title">Source Title</cite></small>
                    </blockquote>
                    <div class="m-t-sm">Lorem ipsum dolor sit amet, consecteter adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</div>
                  </section>
                </article>
              </section>
              <h4 class="m-t-lg m-b">Leave a comment</h4>
              <form>
                <div class="form-group pull-in clearfix">
                  <div class="col-sm-6">
                    <label>Your name</label>
                    <input type="text" class="form-control" placeholder="Name">
                  </div>
                  <div class="col-sm-6">
                    <label >Email</label>
                    <input type="email" class="form-control" placeholder="Enter email">
                  </div>
                </div>
                <div class="form-group">
                  <label>Comment</label>
                  <textarea class="form-control" rows="5" placeholder="Type your comment"></textarea>
                </div>
                <div class="form-group">
                  <button type="submit" class="btn btn-success">Submit comment</button>
                </div>
              </form>
            </div>
            <div class="col-sm-3">
	      <a href="#add-toolbox" data-toggle="modal" class="btn btn-success btn-lg">Add To Toolbox<i class="icon-plus"></i></a>
	      <br>
	      <br>
	      <h5 class="font-semibold">Stats</h5>

	      <button class="btn btn-white">
                  <span class="text">
                    Beta Toolbox Adds: <strong>23</strong></i> 
                  </span>  
                </button>
	         <button class="btn btn-white">
                  <span class="text">
                   Date Added : <strong>11/25/2013</strong></i> 
                  </span>  
                </button>
		 <br>
		  <br>


              <h5 class="font-semibold">About Developer</h5>
              <div class="line line-dashed"></div>
              <div class="m-b-lg">
                <span class="pull-left thumb-sm avatar m-r-sm m-t-xs">
                  <img src="images/nick.jpg" class="img-circle">
                </span>
                <p class="clear text-sm">
                  <a href="profile.php" class="text-info">@nick</a> : Developer at VerifIp, Working on Beta Toolbox to make super good things for the world.
                </p>
              </div>
              <div class="line line-dashed"></div>
              <div class="m-t-sm m-b-lg">
                <a href="#" title="RSS" class="btn btn-rounded btn-warning btn-icon"><i class="icon-rss"></i></a>
                <a href="#" title="Twitter" class="btn btn-rounded btn-twitter btn-icon"><i class="icon-twitter"></i></a>
                <a href="#" title="Facebook" class="btn btn-rounded btn-facebook btn-icon"><i class="icon-facebook"></i></a>
                <a href="#" title="Google+" class="btn btn-rounded btn-gplus btn-icon"><i class="icon-google-plus"></i></a>
                <a href="#" title="LinkedIn" class="btn btn-rounded btn-info btn-icon"><i class="icon-linkedin"></i></a>
              </div>
              <h5 class="font-semibold">Similar Results</h5>
              <div class="line line-dashed"></div>       
           
              <ul class="list-unstyled m-b-lg">
                <li>
                    <p>JQuery Data Distance : description of this similar one  </p>
                    <small class="block text-muted"><i class="icon-time"></i>2 minuts ago</small>
                    <div class="line"></div>
                </li>
                <li>
                    <p>Javascript Distance Data : nunc condimentum ipsum dolor sit amet, consectetur</p>
                    <small class="block text-muted"><i class="icon-time"></i>1 hour ago</small>
                    <div class="line"></div>
                </li>
                <li>
                    <p>JQuery Fixed Distance Fix : nunc condimentum ipsum dolor sit amet, consectetur</p>
                    <small class="block text-muted"><i class="icon-time"></i>3 Days ago</small>
                </li>
              </ul>
             
              
              
                </article>
              </div>
            </div>
          </div>
        </section>
      </section>
      <a href="#" class="hide nav-off-screen-block" data-toggle="class:nav-off-screen" data-target="#nav"></a>
    </section>
    <!-- /.vbox -->
  </section>
<?php require("footer.php"); ?>