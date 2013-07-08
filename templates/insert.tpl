<form action="/created_row" method="POST">
  %for key in cols:
  <span>{{key}}</span>
  <input type="text" name="{{key}}"/>
  %end
  <input type="submit" value="Create row" />
</form> 

%rebase templates/base.tpl title="Create Row"
      
