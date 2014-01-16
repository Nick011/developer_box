   <!-- Create Bucket -->
   <div class="modal fade" id="add-bucket">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body">
          <div class="row">
            <div class="col-sm-12 b-r">
              <h3 class="m-t-none m-b">Add Bucket</h3>
              <p>Create a label for your new bucket.</p>
              <form role="form">
                <div class="form-group">
                  <label>Bucket Name</label>
                  <input type="bucket" class="form-control" placeholder="Example :  Ruby on Rails, Javascript, PHP, Python...">
                </div>
                
                <div class="checkbox m-t-lg">
                  <button type="submit" class="btn btn-sm btn-success pull-right text-uc m-t-n-xs"><strong>Create Bucket</strong></button>
		  <button style="margin-right:5px;" type="submit" class="btn btn-sm btn-default pull-right text-uc m-t-n-xs">Cancel</button>
                </div>                
              </form>
            </div>
            
          </div>          
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
  </div>
   <!-- End Create Bucket -->
   <!-- Toolbox Add -->
   <div class="modal fade" id="add-toolbox">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body">
          <div class="row">
            <div class="col-sm-12 b-r">
              <h3 class="m-t-none m-b">Add To Toolbox</h3>
              <p>Add to a specific toolbox</p>
              <form role="form">
                <div class="form-group">
                    <div class="form-group">
                      <label class="col-sm-2 control-label">Select</label>
                      <div class="col-sm-10">
                        <select name="account" class="form-control m-b">
                          {% for bucket in user.bucket %}
                          <option>All</option>
                          <option>Python</option>
                          <option>Ruby on Rails</option>
                          <option>Javascript</option>
                        </select>
                     
                      </div>
                    </div>
		    		  <div class="line line-dashed line-lg pull-in"></div>

                </div>
		
                
                <div class="checkbox m-t-lg">
                  <button type="submit" class="btn btn-sm btn-success pull-right text-uc m-t-n-xs"><strong>Add  To Toolbox</strong></button>
		  <button style="margin-right:5px;" type="submit" class="btn btn-sm btn-default pull-right text-uc m-t-n-xs">Cancel</button>
                </div>                
              </form>
            </div>
            
          </div>          
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
  </div>
   <!-- End Create Bucket -->
   

  
  <script src="js/jquery.min.js"></script>
  
  <script type="text/javascript" src="js/clipboard/jquery.zclip.js"></script>
  <script>
  $(document).ready(function(){

    $('a#copy-script').zclip({
        path:'js/clipboard/ZeroClipboard.swf',
        copy:$('pre#script').text()
    });

    // The link with ID "copy-description" will copy
    // the text of the paragraph with ID "description"

});
  
  </script>


  
  <!-- Bootstrap -->
  <script src="js/bootstrap.js"></script>
  <!-- App -->
  <script src="js/app.js"></script>
  <script src="js/app.plugin.js"></script>
  <script src="js/app.data.js"></script>
  <!-- Fuelux -->
  <script src="js/fuelux/fuelux.js"></script>
  <script src="js/libs/jquery.pjax.js" cache="false"></script>

    <!-- fuelux -->
  <script src="js/fuelux/fuelux.js"></script>
  <!-- datepicker -->
  <script src="js/datepicker/bootstrap-datepicker.js"></script>
  <!-- slider -->
  <script src="js/slider/bootstrap-slider.js"></script>
  <!-- file input -->  
  <script src="js/file-input/bootstrap.file-input.js"></script>
  <!-- combodate -->
  <script src="js/libs/moment.min.js"></script>
  <script src="js/combodate/combodate.js" cache="false"></script>
  <!-- parsley -->
  <script src="js/parsley/parsley.min.js" cache="false"></script>
  <script src="js/parsley/parsley.extend.js" cache="false"></script>
  <!-- select2 -->
  <script src="js/select2/select2.min.js" cache="false"></script>
  <!-- wysiwyg -->
  <script src="js/wysiwyg/jquery.hotkeys.js" cache="false"></script>
  <script src="js/wysiwyg/bootstrap-wysiwyg.js" cache="false"></script>
  <script src="js/wysiwyg/demo.js" cache="false"></script>


  <script>
  $(document).ready(function(){

     $("#e9").select2();

    });
</script>


</body>
</html>