%if processed_ids:
    <table>
      <tr>
        <th>Spread Id</th>
        <th>Worksheet Ids</th>
      </tr>
      %for i in range(len(spreadsheet_feed.entry)):
          <tr>
            <td>{{spreadsheet_feed.entry[i].title.text}}</td>
            <td>{{processed_ids[i]}}</td>
            %end
          </tr>
    </table>
      
<form action="/set_spreadsheet" method="POST">
  <input type="text" name="set_spreadid" />
  <input type="text" name="set_workid" />
  <input type="submit" value="Set Ids" />
</form>

%rebase templates/base.tpl title="Set Spreadsheet"
      
