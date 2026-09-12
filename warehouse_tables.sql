-- Data warehousing use case for ERPNext Businesses in need of a data engineering stack

CREATE TABLE sales_invoice_dim (
    name VARCHAR(140) NOT NULL,
    creation DATETIME(6),
    modified DATETIME(6),
    posting_date DATE,
    due_date DATE,
    posting_time TIME(6),
    docstatus INT(1),
    customer VARCHAR(140),
    company VARCHAR(140),
    pos_profile VARCHAR(140),
    status VARCHAR(140),
    is_return INT(1),
    currency VARCHAR(100),
    base_grand_total decimal(21,9),
    outstanding_amount DECIMAL(21,9),
    total_taxes_and_charges DECIMAL(21,9)
)


CREATE TABLE sales_figures_facts (
    invoice_id VARCHAR(140) NOT NULL,
    posting_date DATE NOT NULL,
    due_date DATE NOT NULL,
    base_grand_total DECIMAL(21,9) NOT NULL,
    month INT(2) NOT NULL,
    

)



--- Define the pipeline for moving data from source to target (source to dimensions, then later to facts table)
INSERT INTO warehouse_demo.sales_invoice_dim
    ( name,
     creation, 
     modified,
     posting_date, 
     due_date, 
     posting_time, 
     docstatus, 
     customer, 
     company, 
     pos_profile, 
     status, 
     is_return, 
     currency, 
     base_grand_total, 
     outstanding_amount, 
     total_taxes_and_charges
 ) 
SELECT name, 
    creation, 
    modified, 
    posting_date,
    due_date, 
    posting_time, 
    docstatus, 
    customer, 
    company, 
    pos_profile, 
    status, 
    is_return,
    currency, 
    base_grand_total,
    outstanding_amount, 
    total_taxes_and_charges 
    FROM mujengodb.`tabSales Invoice` 
    WHERE posting_date >= '2025-06-01';


-- For slowly changing dimensions (SCD) to capture changes happeing on the source tables, we'll implement the code below in PostgreSQL.

MERGE INTO warehouse_demo.sales_invoice_dim AS target
USING mujengodb.`tabSales Invoice` AS source
ON target.name = source.name 

WHEN MATCHED THEN
UPDATE SET
    target.status = source.status 
    target.outstanding_amount = source.outstanding_amount
    target.modified = source.modified 

WHEN NOT MATCHED THEN
    INSERT (
        name,
        creation,
        modified,
        posting_date,
        due_date,
        posting_time,
        docstatus,
        customer, 
        company,
        pos_profile,
        status,
        is_return,
        currency,
        base_grand_total,
        outstanding_amount,
        total_taxes_and_charges
    )
    VALUES( 
        source.name,
        source.creation,
        source.modified,
        source.posting_date,
        source.due_date,
        source.posting_time,
        source.docstatus,
        source.customer,
        source.company,
        source.pos_profile,
        source.status,
        source.is_return,
        source.currency, 
        source.base_grand_total,
        source.outstanding_amount,
        source.total_taxes_and_charges
    );

--- However, apparently MySQL does not support the MERGE INTO yet, so our query will be as below:


