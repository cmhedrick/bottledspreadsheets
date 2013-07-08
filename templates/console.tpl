<table>
  <tr>
  %for header in keys:
    <th>{{header}}</th>
    %end
  </tr>
  %for row in row_list:
  <tr>
    %for data in row:
    <td>{{data}}</td>
    %end
  %end
  </tr>
</table>     

<a href="/insert_row">Insert Row</a>

%rebase templates/base.tpl title="Console"
      
