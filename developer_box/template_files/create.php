<?php require("header.php"); ?>
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
                    <h2 class="post-title">Create New Toolbox</h2>

                  <div class="panel-body">
                  <form class="form-horizontal" method="get">
                    <div class="form-group">
                      <label class="col-sm-2 control-label">What does it do?</label>
                      <div class="col-sm-10">
                        <input type="text" class="form-control">
                        <span class="help-block m-b-none">What's does it do? Simple title of your script. Ex. "JQuery Distance Between Two Dates Script"</span>
                      </div>
                    </div>

                    <div class="form-group">
                      <label class="col-sm-2 control-label">Code Snippet</label>
                      <div class="col-sm-10">
                        <textarea id="script" class="prettyprint lang-html" style="width:100%;height:220px;"></textarea>
                      </div>
                    </div>

                      <div class="form-group">
                      <label class="col-sm-2 control-label">Description</label>
                      <div class="col-sm-10">
                        <div class="btn-toolbar m-b-sm btn-editor" data-role="editor-toolbar" data-target="#editor">
                             
                          <div class="btn-group" style="padding-bottom:10px;">
                            <a class="btn btn-white btn-sm" data-edit="bold" title="Bold (Ctrl/Cmd+B)"><i class="icon-bold"></i></a>
                            <a class="btn btn-white btn-sm" data-edit="italic" title="Italic (Ctrl/Cmd+I)"><i class="icon-italic"></i></a>
                            <a class="btn btn-white btn-sm" data-edit="strikethrough" title="Strikethrough"><i class="icon-strikethrough"></i></a>
                            <a class="btn btn-white btn-sm" data-edit="underline" title="Underline (Ctrl/Cmd+U)"><i class="icon-underline"></i></a>
                          </div>
                          
                        <div id="editor" class="form-control" style="overflow:scroll;height:150px;max-height:150px">
                          
                        </div>
                        <span class="help-block m-b-none">Description of your script and how to use it.</span>

                         </div>
                    </div>
                    </div>

                    <div class="form-group">
                      <label class="col-sm-2 control-label">Tags</label>
                      <div class="col-sm-10">
      
                            <select multiple="" name="e9" id="e9" style="width:100%" class="populate select2-offscreen" tabindex="-1">
                           <optgroup label="Server Side">
                               <option value="AK">PHP</option>
                               <option value="HI">Ruby on Rails</option>
                               <option value="HI">Python</option>
                               <option value="HI">Cold Fusion</option>
                               <option value="HI">ASP.NET</option>
                           </optgroup>
                           <optgroup label="Client Side">
                               <option value="CA">JQuery</option>
                               <option value="NV">Javascript</option>
                               <option value="OR">CoffeeScript</option>
                               <option value="OR">HTML5</option>
                               <option value="OR">CSS</option>
                               <option value="OR">Browser Fixes</option>
                           </optgroup>
                           <optgroup label="Database">
                               <option value="CA">MySQL</option>
                               <option value="NV">SQL</option>
                               <option value="OR">NuDB</option>
                           </optgroup>
                          </select>
                      </div>
                    </div>


                    <div class="form-group">
                      <label class="col-sm-2 control-label">Add To Bucket</label>
                      <div class="col-sm-10">              
                        
                        <div class="btn-group m-r">
                          <button data-toggle="dropdown" class="btn btn-sm btn-white dropdown-toggle">
                            <span class="dropdown-label" data-placeholder="Please select">Select Bucket</span> 
                            <span class="caret"></span>
                          </button>
                          <ul class="dropdown-menu dropdown-select">
                              <li><a href="#"><input type="checkbox" name="d-s-c-1">PHP</a></li>
                              <li><a href="#"><input type="checkbox" name="d-s-c-2">Ruby on Rails</a></li>
                              <li><a href="#"><input type="checkbox" name="d-s-c-3">Javascript</a></li>
                              <li><a href="#"><input type="checkbox" name="d-s-c-4">JQuery</a></li>
                              <li><a href="#"><input type="checkbox" name="d-s-c-5">Python</a></li>
                          </ul>
                        </div>
                      </div>
                    </div>
                    <br>
                    <br>
                    <div class="line"></div>
                     <div class="form-group">
                              <label class="col-sm-2 control-label"></label>
                              <div class="col-sm-10">
                                <div class="form-group" style="padding-left:15px;">
                                  <button type="submit" class="btn btn-success">Add Toolbox Yippee!</button>
                                </div>
                              </div>
                    </div>
                    </div>
                  </form>
                  </div>
             
                    <div class="line line-lg"></div>
                    <div class="text-muted">
                      
                    </div>
                  </div>
                </div>
                
              </div>
           
            <div class="col-sm-3">
	     
              <h5 class="font-semibold">Recently Created</h5>
              <div class="line line-dashed"></div>       
           
              <ul class="list-unstyled m-b-lg">
                <li>
                    <p><a href="#">JQuery Data Distance : description of this similar one </a> </p>
                    <small class="block text-muted"><i class="icon-time"></i>2 minuts ago</small>
                    <div class="line"></div>
                </li>
                <li>
                    <p>Javascript Distance Data : nunc condimentum ipsum dolor sit amet, consectetur</p>
                    <small class="block text-muted"><i class="icon-time"></i>1 hour ago</small>
                    <div class="line"></div>
                </li>
                </ul>
<br>
              <h5 class="font-semibold">Similar Results</h5>
              <div class="line line-dashed"></div>       
           
              <ul class="list-unstyled m-b-lg">
                <li>
                    <p><a href="#">JQuery Data Distance : description of this similar one </a> </p>
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
                                        <div class="line"></div>

                </li>
                <li>
                    <p>Javascript Distance Data : nunc condimentum ipsum dolor sit amet, consectetur</p>
                    <small class="block text-muted"><i class="icon-time"></i>1 hour ago</small>
                    <div class="line"></div>
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