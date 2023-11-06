﻿using FileStorageApp.Server.Entity;
using Microsoft.EntityFrameworkCore;

namespace FileStorageApp.Server.Database
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions options) : base(options)
        {

        }

        public DbSet<Entity.User> Users { get; set; }
        public DbSet<Entity.Role> Roles { get; set; }
        public DbSet<Entity.FileMetadata> FilesMetadata { get; set; }
        public DbSet<Entity.Challenge> Challenges { get; set; }
        public DbSet<Entity.Resp> Resps { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<User>()
                .HasMany(x => x.Roles)
                .WithMany(y => y.Users)
                .UsingEntity(j => j.ToTable("UserRoles"));
        }
    }
}