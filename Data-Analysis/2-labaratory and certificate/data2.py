# test1
select billingcountry, Count(*) as number_invoices from Invoice
group by 1
order by 2 desc

# test2
select billingcity,sum(total) as invoice_totals from Invoice
group by 1
order by 2 Desc
limit 1

# test3
select c.CustomerId,
c.FirstName,
c.LastName,
sum(inv.UnitPrice) as invoices
from Invoice i
join InvoiceLine inv
on inv.Invoiceid = i.Invoiceid
join customer c
on c.customerid = i.customerid
group by c.CustomerId,c.FirstName,c.LastName
order by i.total desc
limit 1

# test4
Select C.Email,C.FirstName,C.LastName,G.Name
from Customer C
Join Invoice I
On C.CustomerId = I.CustomerId
Join InvoiceLine Inv
On I.InvoiceId = Inv.InvoiceId
Join track T
On T.TrackId = Inv.TrackId
Join Genre G
On G.GenreId = T.GenreId
where G.Name = 'Rock'
group by Email

# test5
with c as(select Invoice.CustomerId as id_cst, Invoice.BillingCountry as Country, sum(Invoice.Total) as som from Invoice
join Customer on Invoice.BillingCountry = Customer.Country and Invoice.CustomerId = Customer.CustomerId
group by 1,2
order by 2 ),
Customers as (select Customer.CustomerId as cust_id, Customer.FirstName as name_customer, Customer.LastName as lastname_customer from Customer)

select customers.cust_id, customers.name_customer,customers.lastname_customer, b.country, b.max_som from Customers,
(select a.country as country, max(a.som) as max_som from 
(select Invoice.CustomerId as id_cst, Invoice.BillingCountry as Country, sum(Invoice.Total) as som from Invoice join Customer on Invoice.BillingCountry = Customer.Country and Invoice.CustomerId = Customer.CustomerId
group by 1,2 
order by 2) as a
 group by 1
 order by 2 ) as b
join c
on c.country = b.country and c.som = b.max_som
where Customers.cust_id = c.id_cst