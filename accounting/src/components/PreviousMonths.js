import React from 'react';
import Paper from '@material-ui/core/Paper';
import Container from '@material-ui/core/Container';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TablePagination from '@material-ui/core/TablePagination';

import useStyles from '../styles/AppStyles';
import StyledTableCell from './StyledTableCell';
import CONFIG from '../config';
import { get_month } from '../utils/Month';
import { Typography } from '@material-ui/core';

const columns = [
  { id: 'year', label: 'Year', minWidth: 170 },
  { id: 'month', label: 'Month', minWidth: 170 },
  { id: 'new_providers', label: 'New providers', minWidth: 170 },
  { id: 'updated_providers', label: 'Updated providers', minWidth: 170 },
  { id: 'new_resources', label: 'New resources', minWidth: 170 },
  { id: 'updated_resources', label: 'Updated resources', minWidth: 170 },
  { id: 'new_users', label: 'New users', minWidth: 170 },
];

const createData = (
  month,
  year,
  new_providers,
  updated_providers,
  new_resources,
  updated_resources,
  new_users
) => {
  return {
    month: get_month(month),
    month_num: month,
    year,
    new_providers,
    updated_providers,
    new_resources,
    updated_resources,
    new_users,
  };
};

const compare_date = (a, b) => {
  if (a.year > b.year) {
    return -1;
  } else if (b.year > a.year) {
    return 1;
  } else {
    if (a.month_num > b.month_num) return -1;
    else return 1;
  }
};

const PreviousMonths = () => {
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [rows, setRows] = React.useState([]);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  React.useEffect(() => {
    fetch(`${CONFIG.endpoint}/api/v2/monthly_stats`)
      .then((res) => res.json())
      .then((result) => {
        setRows(
          result
            .map((entry) =>
              createData(
                entry.month,
                entry.year,
                entry.new_providers,
                entry.updated_providers,
                entry.new_resources,
                entry.updated_resources,
                entry.new_users
              )
            )
            .sort(compare_date)
        );
      });
  }, []);

  return (
    <>
      <Container maxWidth="sm" component="main" className={classes.title}>
        <Typography component="h1" variant="h4" color="textPrimary">
          Previous Months
        </Typography>
      </Container>

      <Container maxWidth="lg" className={classes.heroContent}>
        <Paper className={classes.root}>
          <TableContainer className={classes.tableBody}>
            <Table stickyHeader aria-label="sticky table">
              <TableHead>
                <TableRow>
                  {columns.map((column) => (
                    <StyledTableCell key={column.id} align={column.align}>
                      {column.label}
                    </StyledTableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {rows
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row) => {
                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        tabIndex={-1}
                        key={row.year.toString().concat(row.month)}
                      >
                        {columns.map((column) => {
                          const value = row[column.id];
                          return (
                            <TableCell key={column.id} align={column.align}>
                              {column.format && typeof value === 'number'
                                ? column.format(value)
                                : value}
                            </TableCell>
                          );
                        })}
                      </TableRow>
                    );
                  })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[10, 25, 100]}
            component="div"
            count={rows.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onChangePage={handleChangePage}
            onChangeRowsPerPage={handleChangeRowsPerPage}
          />
        </Paper>
      </Container>
    </>
  );
};

export default PreviousMonths;
