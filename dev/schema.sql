CREATE TABLE grants (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  title TEXT NOT NULL,
  funder VARCHAR(255),
  source_url TEXT NOT NULL,
  apply_url TEXT,
  deadline_date DATE,
  eligibility TEXT,
  amount_min DECIMAL(12,2),
  amount_max DECIMAL(12,2),
  retrieved_at DATETIME NOT NULL,
  content_hash CHAR(32) NOT NULL,
  robots_allowed TINYINT(1) DEFAULT 1,
  FULLTEXT KEY ft_title_elig (title, eligibility)
);
